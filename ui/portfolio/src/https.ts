import axios from "axios";

const API_BASE_URL = process.env.VUE_APP_API_BASE_URL;
const http = axios.create({
  baseURL: API_BASE_URL,
  timeout: 5 * 60 * 1000,
  responseType: "json",
});

export default http;
