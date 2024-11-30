import { useState, useRef, useEffect } from "react";

export const getLabel = (allOptions, selectedOptionsValues, parentValue) => {
  // Nothing has been selected yet
  if (!selectedOptionsValues.length) {
    return "Sélectionner une option";
  }

  const optionsLabels = allOptions.map((option) => {
    let optionPath = option.value;
    if (parentValue) optionPath = `${parentValue}.${option.value}`;

    const optionIsSelected = selectedOptionsValues.some(
      (selectedOption) => selectedOption === optionPath,
    );

    if (optionIsSelected) {
      // Option has sub-options
      if (option.options) {
        // Recursive call to get potential sub-options labels (if selected)
        const subOptionsLabels = getLabel(
          option.options,
          selectedOptionsValues,
          optionPath,
        );

        // Some sub-options are indeed selected
        if (subOptionsLabels) {
          return `${option.label} (${subOptionsLabels})`;
        }

        return `${option.label}`;
      } else {
        return option.label;
      }
    }

    return null;
  });

  return optionsLabels.filter(Boolean).join(", ");
};
export const getValuesFromOptions = (options, parentPaths) => {
  let res = [];

  options.forEach((option) => {
    const optionPath = parentPaths.length
      ? [...parentPaths, option.value].join(".")
      : option.value;

    res.push(optionPath);

    // Option has sub-options. Go recursive
    if (option.options) {
      const subOptionsValues = getValuesFromOptions(option.options, [
        ...parentPaths,
        option.value,
      ]);

      res = [...res, ...subOptionsValues];
    }
  });

  return res;
};

const MapOptions = ({
  options,
  parentPaths = [],
  ml = 0,
  onAdd,
  onRemove,
  selected,
}) => (
  <>
    {options.map((option) => {
      const optionPath = parentPaths.length
        ? [...parentPaths, option.value].join(".")
        : option.value;

      return (
        <div key={option.value}>
          <div className={`fr-mb-2v fr-checkbox-group fr-ml-${ml * 8}v`}>
            <input
              id={`id_checkbox—${option.value}`}
              type="checkbox"
              className={`optionCheckbox`}
              name={option.value}
              checked={selected.includes(option.value)}
              onChange={(e) => {
                e.target.checked
                  ? onAdd(e.target.name)
                  : onRemove(e.target.name);
              }}
            />
            <label htmlFor={`id_checkbox—${option.value}`} className="fr-label">
              {option.label}
            </label>
          </div>
          {option.options && (
            <MapOptions
              options={option.options}
              ml={ml + 1}
              onAdd={onAdd}
              onRemove={onRemove}
              selected={selected}
            />
          )}
        </div>
      );
    })}
  </>
);

export const SelectWithSubOptions = ({
  options: allOptions,
  selected,
  onAdd,
  onRemove,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const ref = useRef(null);

  const optionMapping = allOptions.reduce(
    (acc, item) => ({ ...acc, [item.value]: item.shortLabel }),
    {},
  );
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
        {selected.length
          ? `${selected.length} valeurs(s) sélectionnée(s)`
          : "Sélectionner une option"}
      </div>
      {isOpen && (
        <div className="dropDownWrapper">
          <div className="fr-container-fluid">
            <MapOptions
              options={allOptions}
              onAdd={onAdd}
              onRemove={onRemove}
              selected={selected}
            />
          </div>
        </div>
      )}

      <div>
        {selected.map((s) => (
          <button
            className="fr-tag fr-tag--sm fr-tag--dismiss"
            key={s}
            onClick={() => onRemove(s)}
          >
            {optionMapping[s]}
          </button>
        ))}
      </div>
    </div>
  );
};
