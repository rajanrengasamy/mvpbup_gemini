import type { DemoModelRequest, DemoModelResponse } from 'src/core/types/demoModel';
import { axiosClient } from '../client';

export class DemoService {
  static async getDemoModel(request: DemoModelRequest) {
    // Pass query parameters correctly using the Axios config object
    return axiosClient.get<DemoModelResponse>('/demo/model', {
      params: request,
    });
  }
}
