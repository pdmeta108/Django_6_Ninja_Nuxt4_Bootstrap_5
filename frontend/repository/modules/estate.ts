import { HttpFactory } from '../factory';
import type { IEstate, IMunicipality } from '~~/types/estate';

class EstateModule extends HttpFactory {
    private RESOURCE = '/estate';

    /**
     * Fetch all estates
     */
    async getAll(): Promise<IEstate[]> {
        return await this.call<IEstate[]>('GET', `${this.RESOURCE}`);
    }

    /**
     * Fetch municipalities by estate
     */
    async getMunicipalitiesByEstate(estate_id: string | number): Promise<IMunicipality> {
        return await this.call<IMunicipality>('GET', `${this.RESOURCE}/municipalities/${estate_id}`);
    }

    // async create(account: ICreateAccountInput): Promise<ICreateAccountResponse> {
    //     return await this.call<ICreateAccountResponse>('POST', `${this.RESOURCE}/register`, account);
    // }
  }

  export default EstateModule;