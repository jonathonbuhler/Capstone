import { type FilterProps } from "../Filters/Filters";

function Personalization({
  setLaptops,
  page,
  filters,
  setFilters,
}: FilterProps) {
  return <>{filters}</>;
}

export default Personalization;
