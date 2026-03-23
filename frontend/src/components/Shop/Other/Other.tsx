import styles from "./Other.module.css";

function Other() {
  return (
    <div className={styles.other}>
      <div className="dropdown">
        <button
          className="btn btn-primary dropdown-toggle"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          Price Your Laptop
        </button>
        <div className="dropdown-menu">
          <form action="">
            <input type="text" />
          </form>
        </div>
      </div>
    </div>
  );
}

export default Other;
