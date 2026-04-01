import { useState } from "react";
import styles from "./Other.module.css";
import Price from "./Price";
import { type FilterProps } from "../Filters/Filters";
import Personalization from "./Personalization";

function Other({ setLaptops, page, filters, setFilters }: FilterProps) {
  return (
    <div className={styles.other}>
      <Price />
      <Personalization
        setLaptops={setLaptops}
        page={page}
        filters={filters}
        setFilters={setFilters}
      />
    </div>
  );
}

export default Other;
