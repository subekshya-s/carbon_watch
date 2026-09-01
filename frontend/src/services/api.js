import axios from 'axios'

const API = axios.create({
  baseURL: 'https://carbon-watch-jgky.onrender.com/api',
})

export const getDistricts = () => API.get('/districts/')
export const getDistrict = (id) => API.get(`/districts/${id}/`)
export const triggerAnalysis = (id) => API.post(`/districts/${id}/analyze/`)
export const getAnalysis = (id) => API.get(`/analyses/${id}/`)

export default API
