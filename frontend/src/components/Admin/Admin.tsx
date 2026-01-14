import { useState } from "react";
import styles from "./Admin.module.css";

function Admin() {
  const [formData, setFormData] = useState({
    asin: "",
    model_number: "",
    model_name: "",
    brand: "",
    storage_type: "",
    storage_capacity: "",
    cpu: "",
    cpu_cores: "",
    cpu_clock: "",
    ram_type: "",
    ram_capacity: "",
    screen_size: "",
    screen_width: "",
    screen_height: "",
    screen_refresh: "",
    battery_capacity: "",
    price: "",
    year: "",
  });

  const handleSearch = () => {
    fetch(`http://localhost:8000/admin/${formData.asin}`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setFormData(data);
      })
      .catch((err) => console.error(err));
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const name = e.target.name;
    if (!name) {
      return;
    }
    setFormData((prev) => ({ ...prev, [name]: e.target.value }));
  };

  const handleAdd = () => {
    fetch("http://localhost:8000/admin/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).catch((err) => console.error(err));
  };

  return (
    <div className="main-container">
      <div className={styles["add-data"]}>
        <h1>Admin</h1>
        <div className={styles.search}>
          <input
            type="text"
            name="asin"
            id="asin"
            placeholder="ASIN"
            value={formData.asin}
            onChange={handleChange}
          />
          <button onClick={handleSearch}>Search</button>
        </div>
        <hr />
        <div className={styles.features}>
          <input
            type="text"
            placeholder="Model Number"
            name="model_number"
            value={formData.model_number}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Model Name"
            name="model_name"
            value={formData.model_name}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Brand"
            name="brand"
            value={formData.brand}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Storage Type"
            name="storage_type"
            value={formData.storage_type}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Storage Capacity"
            name="storage_capacity"
            value={formData.storage_capacity}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="CPU"
            name="cpu"
            value={formData.cpu}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="CPU Cores"
            name="cpu_cores"
            value={formData.cpu_cores}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="CPU Clock"
            name="cpu_clock"
            value={formData.cpu_clock}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Ram Type"
            name="ram_type"
            value={formData.ram_type}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Ram Capacity"
            name="ram_capacity"
            value={formData.ram_capacity}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Screen Size"
            name="screen_size"
            value={formData.screen_size}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Screen Width"
            name="screen_width"
            value={formData.screen_width}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Screen Height"
            name="screen_height"
            value={formData.screen_height}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Screen Refresh"
            name="screen_refresh"
            value={formData.screen_refresh}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Battery Capacity"
            name="battery_capacity"
            value={formData.battery_capacity}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Year"
            name="year"
            value={formData.year}
            onChange={handleChange}
          />
          <input
            type="text"
            placeholder="Price"
            name="price"
            value={formData.price}
            onChange={handleChange}
          />
          <button onClick={handleAdd}>Add</button>
        </div>
      </div>
    </div>
  );
}

export default Admin;
