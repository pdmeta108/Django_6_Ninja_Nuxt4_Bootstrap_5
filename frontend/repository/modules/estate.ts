import { HttpFactory } from '../factory';
import type { IEstate, IMunicipality, IParish } from '~~/types/estate';

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

    /**
     * Fetch parishes by municipality
     */
    async getParishesByMunicipality(municipality_id: string | number): Promise<IParish> {
        return await this.call<IParish>('GET', `${this.RESOURCE}/parishes/${municipality_id}`);
    }

    // async create(account: ICreateAccountInput): Promise<ICreateAccountResponse> {
    //     return await this.call<ICreateAccountResponse>('POST', `${this.RESOURCE}/register`, account);
    // }
  }

  export default EstateModule;