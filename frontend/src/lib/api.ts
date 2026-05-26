import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export interface AnalyzeRequest {
  message: string;
  model_type: string;
  model_name: string;
}

export interface AnalyzeResponse {
  intent: string;
  confidence: number;
  entities: Record<string, string>;
  answer?: string;
}

export const analyze = async (
  data: AnalyzeRequest
): Promise<AnalyzeResponse> => {
  const response = await api.post("/analyze", data);
  return response.data;
};
