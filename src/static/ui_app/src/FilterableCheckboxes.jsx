import { useState, useRef, useEffect } from "react";

// export const getLabel = (allOptions, selectedOptionsValues, parentValue) => {
//   // Nothing has been selected yet
//   if (!selectedOptionsValues.length) {
//     return "Sélectionner une option";
//   }
//
//   const optionsLabels = allOptions.map((option) => {
//     let optionPath = option.value;
//     if (parentValue) optionPath = `${parentValue}.${option.value}`;
//
//     const optionIsSelected = selectedOptionsValues.some(
//       (selectedOption) => selectedOption === optionPath,
//     );
//
//     if (optionIsSelected) {
//       // Option has sub-options
//       if (option.options) {
//         // Recursive call to get potential sub-options labels (if selected)
//         const subOptionsLabels = getLabel(
//           option.options,
//           selectedOptionsValues,
//           optionPath,
//         );
//
//         // Some sub-options are indeed selected
//         if (subOptionsLabels) {
//           return `${option.label} (${subOptionsLabels})`;
//         }
//
//         return `${option.label}`;
//       } else {
//         return option.label;
//       }
//     }
//
//     return null;
//   });
//
//   return optionsLabels.filter(Boolean).join(", ");
// };

export const getValuesFromOptions = ({ options, parentPaths = [] }) => {
  let res = [];

  options.forEach((option) => {
    const optionPath = parentPaths.length
      ? [...parentPaths, option.value].join(".")
      : option.value;

    res.push(optionPath);

    // Option has sub-options. Go recursive
    if (option.options) {
      const subOptionsValues = getValuesFromOptions({
        options: option.options,
        parentPaths: [...parentPaths, option.value],
      });

      res = [...res, ...subOptionsValues];
    }
  });

  return res;
};

const MapOptions = ({
  options,
  filterKey,
  subFilterKey = "root",
  parentPaths = [],
  ml = 0,
  onAdd,
  onRemove,
  selected,
}) => {
  return (
    <>
      {options.map((option) => {
        return (
          <div key={option.value}>
            <div className={`fr-mb-2v fr-checkbox-group fr-ml-${ml * 8}v`}>
              <input
                id={`id_checkbox—${option.value}`}
                type="checkbox"
                className={`optionCheckbox`}
                name={option.value}
                checked={selected[subFilterKey].includes(option.value)}
                onChange={(e) => {
                  e.target.checked
                    ? onAdd({
                        filterKey: filterKey,
                        subFilterKey: subFilterKey,
                        value: e.target.name,
                      })
                    : onRemove({
                        filterKey: filterKey,
                        subFilterKey: subFilterKey,
                        value: e.target.name,
                      });
                }}
              />
              <label
                htmlFor={`id_checkbox—${option.value}`}
                className="fr-label"
              >
                {option.label}
              </label>
            </div>
            {option.options &&
              selected[subFilterKey].includes(option.value) && (
                <MapOptions
                  options={option.options}
                  filterKey={filterKey}
                  subFilterKey={option.subTypesName}
                  ml={ml + 1}
                  onAdd={onAdd}
                  onRemove={onRemove}
                  selected={selected}
                  parentPaths={[...parentPaths, option.value]}
                />
              )}
          </div>
        );
      })}
    </>
  );
};

const buildOptionMapping = (options) =>
  options.reduce(
    (acc, item) => ({
      ...acc,
      [item.value]: item.shortLabel,
      ...(item.options ? buildOptionMapping(item.options) : {}),
    }),
    {},
  );

export const FilterableCheckboxes = ({
  options: allOptions,
  filterKey,
  subFilterKey = "root",
  selected,
  onAdd,
  onRemove,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const ref = useRef(null);

  const optionMapping = buildOptionMapping(allOptions);

  useEffect(() => {
    // Close select if user clicks elsewhere in the page
    const handleClickInPage = (e) => {
      if (ref.current && !ref.current.contains(e.target)) {
        if (isOpen) setIsOpen(false);
      }
    };
    if (isOpen) {
      window.addEventListener("click", handleClickInPage);

      return () => {
        window.removeEventListener("click", handleClickInPage);
      };
    }
  }, [isOpen]);
  return (
    <div className="fr-mt-2v select-wrapper" ref={ref}>
      <div
        role={"button"}
        tabIndex={0}
        className={`fr-select select ${isOpen ? "select-open" : ""}`}
        onClick={() => setIsOpen(!isOpen)}
        // onKeyDown={handleKeyDown}
        aria-expanded={isOpen}
      >
        {selected[subFilterKey].length
          ? `${selected[subFilterKey].length} valeurs(s) sélectionnée(s)`
          : "Sélectionner une option"}
      </div>
      {isOpen && (
        <div className="dropDownWrapper">
          <div className="fr-container-fluid">
            <MapOptions
              options={allOptions}
              onAdd={onAdd}
              filterKey={filterKey}
              onRemove={onRemove}
              selected={selected}
            />
          </div>
        </div>
      )}

      <div>
        {/*{selected.root.map((s) => (*/}
        {/*  <button*/}
        {/*    className="fr-tag fr-tag--sm fr-tag--dismiss"*/}
        {/*    key={s}*/}
        {/*    onClick={() =>*/}
        {/*      onRemove({*/}
        {/*        filterKey: filterKey,*/}
        {/*        subFilterKey: "root",*/}
        {/*        value: s,*/}
        {/*      })*/}
        {/*    }*/}
        {/*  >*/}
        {/*    {optionMapping[s]}*/}
        {/*  </button>*/}
        {/*))}*/}
        {Object.entries(selected).map(([subFilterKey, items]) =>
          items.map((s) => (
            <button
              className="fr-tag fr-tag--sm fr-tag--dismiss"
              key={s}
              onClick={() =>
                onRemove({
                  filterKey: filterKey,
                  subFilterKey,
                  value: s,
                })
              }
            >
              {optionMapping[s]}
            </button>
          )),
        )}
      </div>
    </div>
  );
};
