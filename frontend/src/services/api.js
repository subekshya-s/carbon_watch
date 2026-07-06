import axios from 'axios'

const API = axios.create({
  baseURL: 'http://localhost:8000/api',
})

export const getDistricts = () => API.get('/districts/')
export const getDistrict = (id) => API.get(`/districts/${id}/`)
export const triggerAnalysis = (id) => API.post(`/districts/${id}/analyze/`)
export const getAnalysis = (id) => API.get(`/analyses/${id}/`)

export default API
