import { useState } from "react";
import styles from "./Other.module.css";

function Price() {
  const [laptop, setLaptop] = useState({
    id: 0,
    asin: "",
    year: 0,
    storage_capacity: 0,
    ram_capacity: 0,
    ram_type: "DDR4",
    dedicated_gpu: false,
    cpu_cores: 0,
    cpu_clock: 0,
    touch_screen: false,
    screen_size: 0,
    screen_width: 0,
    screen_height: 0,
    screen_refresh: 0,
    battery_capacity: 0,
    fair_price: 0,
  });

  const handleSubmit = (
    e: React.MouseEvent<HTMLButtonElement> | React.FormEvent<HTMLFormElement>,
  ) => {
    e.preventDefault();
    e.stopPropagation();
    fetch("http://localhost:8000/predict-fair", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(laptop),
    })
      .then((res) => res.json())
      .then((data) => {
        setLaptop({ ...laptop, fair_price: data.fair_price });
      })
      .catch((err) => console.error(err));
  };

  const handleChange = (
    e:
      | React.ChangeEvent<HTMLInputElement>
      | React.ChangeEvent<HTMLSelectElement>,
  ) => {
    let name = e.target.name;
    let value: number | boolean | string = e.target.value;
    if (name == "dedicated_gpu" || name == "touch_screen") {
      if (value == "false") {
        value = false;
      }
      if (value == "true") {
        value = true;
      }
    } else if (name != "ram_type") {
      value = parseFloat(value);
    }
    setLaptop({ ...laptop, [name]: value });
  };
  return (
    <div className="dropdown">
      <button
        className="btn dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
        data-bs-auto-close="outside"
      >
        Price Your Laptop
      </button>
      <div className="dropdown-menu">
        <form className={styles.form} onSubmit={handleSubmit}>
          <label htmlFor="year">Year</label>
          <input
            value={laptop.year}
            onChange={handleChange}
            type="number"
            name="year"
            placeholder="Year"
          />
          <label htmlFor="storage_capacity">Storage Capacity (GB)</label>
          <input
            type="number"
            onChange={handleChange}
            name="storage_capacity"
            placeholder="Storage Capactiy"
          />
          <label htmlFor="ram_capacity">Ram Capacity (GB)</label>
          <input
            name="ram_capacity"
            type="text"
            onChange={handleChange}
            placeholder="Ram Capacity"
          />
          <label htmlFor="ram_type">Ram Type</label>
          <select onChange={handleChange} name="ram_type">
            <option value="DDR3">DDR3</option>
            <option value="DDR4">DDR4</option>
            <option value="DDR5">DDR5</option>
            <option value="LPDDR4">LPDDR4</option>
            <option value="LPDDR5">LPDDR5</option>
          </select>
          <label htmlFor="dedicated_gpu">Dedicated GPU</label>
          <select onChange={handleChange} name="dedicated_gpu">
            <option value="true">No</option>
            <option value="false">Yes</option>
          </select>
          <label htmlFor="cpu_cores">CPU Core Count</label>
          <input
            type="number"
            onChange={handleChange}
            name="cpu_cores"
            placeholder="CPU Core Count"
          />
          <label htmlFor="cpu_clock">CPU Clock Speed (GHz)</label>
          <input
            name="cpu_clock"
            onChange={handleChange}
            type="number"
            placeholder="CPU Clock Speed"
          />
          <label htmlFor="touch_screen">Touchscreen</label>
          <select onChange={handleChange} name="touch_screen">
            <option value="false">No</option>
            <option value="true">Yes</option>
          </select>
          <label htmlFor="screen_size">Screen Size (inches)</label>
          <input
            type="number"
            onChange={handleChange}
            placeholder="Screen Size (inches)"
            name="screen_size"
          />
          <label htmlFor="screen_width">Screen Resolution (pixels)</label>
          <input
            type="number"
            onChange={handleChange}
            placeholder="Screen Width"
            name="screen_width"
          />
          <input
            type="number"
            onChange={handleChange}
            placeholder="Screen Height"
            name="screen_height"
          />
          <label htmlFor="screen_refresh">Screen Refresh Rate (Hz)</label>
          <input
            name="screen_refresh"
            onChange={handleChange}
            type="number"
            placeholder="Screen Refresh Rate"
          />
          <label htmlFor="battery_capacity">Battery Capacity (Wh)</label>
          <input
            name="battery_capacity"
            onChange={handleChange}
            type="number"
            placeholder="Battery Capacity"
          />
          <p>Predicted Fair-Price: ${laptop.fair_price.toFixed(2)}</p>
          <button
            type="submit"
            onClick={handleSubmit}
            className="btn btn-primary"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}

export default Price;
