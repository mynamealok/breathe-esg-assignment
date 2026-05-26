import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {

    const [records, setRecords] = useState([]);

    useEffect(() => {

        api.get("records/")
            .then((res) => {
                setRecords(res.data);
            })
            .catch((error) => {
                console.error(error);
            });

    }, []);

    const approveRecord = async (id) => {

        try {

            await api.post(`approve/${id}/`);

            alert("Record Approved");

            window.location.reload();

        } catch (error) {

            console.error(error);

            alert("Approval Failed");
        }
    };

    const lockRecord = async (id) => {

        try {

            await api.post(`lock/${id}/`);

            alert("Record Locked");

            window.location.reload();

        } catch (error) {

            console.error(error);

            alert("Lock Failed");
        }
    };

    return (

        <div>

            <h2>Activity Records</h2>

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    marginBottom: "20px",
                    flexWrap: "wrap"
                }}
            >

                <div
                    style={{
                        border: "1px solid #ccc",
                        padding: "15px",
                        minWidth: "120px"
                    }}
                >
                    <h3>Total</h3>
                    <h2>{records.length}</h2>
                </div>

                <div
                    style={{
                        border: "1px solid #ccc",
                        padding: "15px",
                        minWidth: "120px"
                    }}
                >
                    <h3>Pending</h3>
                    <h2>
                        {
                            records.filter(
                                r => r.status === "PENDING"
                            ).length
                        }
                    </h2>
                </div>

                <div
                    style={{
                        border: "1px solid #ccc",
                        padding: "15px",
                        minWidth: "120px"
                    }}
                >
                    <h3>Approved</h3>
                    <h2>
                        {
                            records.filter(
                                r => r.status === "APPROVED"
                            ).length
                        }
                    </h2>
                </div>

                <div
                    style={{
                        border: "1px solid #ccc",
                        padding: "15px",
                        minWidth: "120px"
                    }}
                >
                    <h3>Locked</h3>
                    <h2>
                        {
                            records.filter(
                                r => r.status === "LOCKED"
                            ).length
                        }
                    </h2>
                </div>

            </div>

            <table border="1" cellPadding="8">

                <thead>

                <tr>
                    <th>ID</th>
                    <th>Activity</th>
                    <th>Quantity</th>
                    <th>Unit</th>
                    <th>Status</th>
                    <th>Approve</th>
                    <th>Lock</th>
                </tr>

                </thead>

                <tbody>

                {records.map((record) => (

                    <tr key={record.id}>

                        <td>{record.id}</td>
                        <td>{record.activity_type}</td>
                        <td>{record.quantity}</td>
                        <td>{record.unit}</td>
                        <td>{record.status}</td>

                        <td>

                            <button
                                onClick={() =>
                                    approveRecord(record.id)
                                }
                            >
                                Approve
                            </button>

                        </td>

                        <td>

                            <button
                                onClick={() =>
                                    lockRecord(record.id)
                                }
                            >
                                Lock
                            </button>

                        </td>

                    </tr>

                ))}

                </tbody>

            </table>

        </div>
    );
}