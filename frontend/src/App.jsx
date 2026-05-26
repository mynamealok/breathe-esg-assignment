import Upload from "./pages/Upload";
import Dashboard from "./pages/Dashboard";
import Issues from "./pages/Issues";

function App() {

    return (

        <div
            style={{
                padding: "20px",
                fontFamily: "Arial"
            }}
        >

            <h1
                style={{
                    textAlign: "center"
                }}
            >
                Breathe ESG Data Review Dashboard
            </h1>

            <hr />

            <Upload />

            <hr />

            <Dashboard />

            <hr />

            <Issues />

        </div>

    );
}

export default App;