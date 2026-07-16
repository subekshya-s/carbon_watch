import { Link } from "react-router-dom";

export default function LandingPage() {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#081C15",
        color: "white",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1>Carbon Watch</h1>

      <p>Satellite-based Forest Carbon Monitoring for Nepal</p>

      <Link to="/dashboard">
        <button
          style={{
            padding: "12px 25px",
            fontSize: "16px",
            cursor: "pointer",
            marginTop: "20px",
          }}
        >
          Analyze District →
        </button>
      </Link>
    </div>
  );
}