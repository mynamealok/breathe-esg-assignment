import { useEffect, useState } from "react";
import api from "../services/api";

export default function Issues() {

    const [issues, setIssues] = useState([]);

    useEffect(() => {

        api.get("issues/")
            .then((res) => {
                setIssues(res.data);
            })
            .catch((error) => {
                console.error(error);
            });

    }, []);

    return (

        <div>

            <h2>Suspicious Records Review</h2>

            <h3>Total Issues: {issues.length}</h3>

            <table border="1">

                <thead>

                <tr>
                    <th>#</th>
                    <th>Record ID</th>
                    <th>Issue Description</th>
                </tr>

                </thead>

                <tbody>

                {issues.length === 0 ? (

                    <tr>
                        <td colSpan="3">
                            No Issues Found
                        </td>
                    </tr>

                ) : (

                    issues.map((issue, index) => (

                        <tr key={index}>

                            <td>{index + 1}</td>

                            <td>{issue.record_id}</td>

                            <td>{issue.issue}</td>

                        </tr>

                    ))

                )}

                </tbody>

            </table>

        </div>
    );
}