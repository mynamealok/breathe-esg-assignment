import { useState } from "react";
import api from "../services/api";

export default function Upload() {

    const [file, setFile] = useState(null);

    const uploadSAP = async () => {

        if (!file) {
            alert("Please select a file");
            return;
        }

        try {

            const formData = new FormData();

            formData.append("file", file);

            await api.post(
                "upload/sap/",
                formData
            );

            alert("SAP File Uploaded Successfully");

        } catch (error) {

            console.error(error);

            alert("SAP Upload Failed");
        }
    };

    const uploadUtility = async () => {

        if (!file) {
            alert("Please select a file");
            return;
        }

        try {

            const formData = new FormData();

            formData.append("file", file);

            await api.post(
                "upload/utility/",
                formData
            );

            alert("Utility File Uploaded Successfully");

        } catch (error) {

            console.error(error);

            alert("Utility Upload Failed");
        }
    };

    const uploadTravel = async () => {

        if (!file) {
            alert("Please select a file");
            return;
        }

        try {

            const formData = new FormData();

            formData.append("file", file);

            await api.post(
                "upload/travel/",
                formData
            );

            alert("Travel File Uploaded Successfully");

        } catch (error) {

            console.error(error);

            alert("Travel Upload Failed");
        }
    };

    return (

        <div>

            <h2>Data Upload Center</h2>

            <input
                type="file"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <br /><br />

            <button onClick={uploadSAP}>
                Upload SAP CSV
            </button>

            <button
                onClick={uploadUtility}
                style={{ marginLeft: "10px" }}
            >
                Upload Utility CSV
            </button>

            <button
                onClick={uploadTravel}
                style={{ marginLeft: "10px" }}
            >
                Upload Travel CSV
            </button>

        </div>
    );
}