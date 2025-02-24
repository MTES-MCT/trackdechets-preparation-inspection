import { FilterableCheckboxes } from "../FilterableCheckboxes.jsx";

import { PROFILE_OPTIONS } from "../constants";

const Departments = () => {
  return (
    <FilterableCheckboxes
      options={PROFILE_OPTIONS}
      filterKey="bsdFilters"
      selected={[]}
      onAdd={() => 1}
      onRemove={() => 1}
      onClear={() => null}
    />
  );
};

export default Departments;
