import { PROFILE_OPTIONS } from "../constants";

const Profiles = ({ options }) => {
  return PROFILE_OPTIONS.map((option) => {
    const ml = 1;
    return (
      <div key={option.value}>
        <div className={`fr-mb-2v fr-checkbox-group fr-ml-${ml * 8}v`}>
          <input
            id={`id_checkbox—${option.value}`}
            type="checkbox"
            className={`optionCheckbox`}
            name={option.value}
            // checked={selected[subFilterKey].includes(option.value)}
            // onChange={(e) => {
            //   e.target.checked
            //     ? onAdd({
            //         filterKey: filterKey,
            //         subFilterKey: subFilterKey,
            //         value: e.target.name,
            //       })
            //     : onRemove({
            //         filterKey: filterKey,
            //         subFilterKey: subFilterKey,
            //         value: e.target.name,
            //       });
            // }}
          />
          <label htmlFor={`id_checkbox—${option.value}`} className="fr-label">
            {option.label}
          </label>
        </div>
        {/*{option.options &&*/}
        {/*  selected[subFilterKey].includes(option.value) && (*/}
        {/*    <MapOptions*/}
        {/*      options={option.options}*/}
        {/*      filterKey={filterKey}*/}
        {/*      subFilterKey={option.subTypesName}*/}
        {/*      ml={ml + 1}*/}
        {/*      onAdd={onAdd}*/}
        {/*      onRemove={onRemove}*/}
        {/*      selected={selected}*/}
        {/*      parentPaths={[...parentPaths, option.value]}*/}
        {/*    />*/}
        {/*  )}*/}
      </div>
    );
  });
};

export default Profiles;
