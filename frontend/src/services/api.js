import axios from "axios";

const api = axios.create({
    baseURL: "https://breathe-esg-assignment-production-5f11.up.railway.app/api/"
});
export default api;