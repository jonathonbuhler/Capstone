import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { blank_laptop, type Laptop } from "../../../helpers/Laptop";
import styles from "./LaptopView.module.css";

function LaptopView() {
  const { id } = useParams();
  const [laptop, setLaptop] = useState<Laptop>(blank_laptop);

  useEffect(() => {
    fetch(`http://localhost:8000/laptop/${id}`)
      .then((res) => res.json())
      .then((data) => setLaptop(data));
  }, []);

  return (
    <div className="main-container">
      <div className={styles.laptopv}>
        <h1>{laptop.title}</h1>
        <h2>
          <a href={`https://amazon.com/dp/${laptop.asin}`}>Amazon</a>
        </h2>
        <p>${laptop.price.toFixed(2)}</p>
        <p>${laptop.fair_price.toFixed(2)}</p>
        <img src={laptop.img_url} alt="" />
        <p>
          RAM: {laptop.ram_capacity} GB {laptop.ram_type}
        </p>
        <p>
          Display: {laptop.screen_size}", {laptop.screen_width} x{" "}
          {laptop.screen_height}, {laptop.screen_refresh} Hz,{" "}
          {laptop.touch_screen ? "Touchscreen" : ""}
        </p>

        <p>Storage: {laptop.storage_capacity} GB</p>
        <p>
          CPU: {laptop.cpu_clock} GHz, {laptop.cpu_cores} Core,{" "}
          {laptop.cpu}{" "}
        </p>
        <p>
          GPU: {laptop.dedicated_gpu ? "Dedicated" : "Integrated"} {laptop.gpu}
        </p>
      </div>
    </div>
  );
}

export default LaptopView;
