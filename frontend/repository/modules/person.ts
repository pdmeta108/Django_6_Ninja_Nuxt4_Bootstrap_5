import { HttpFactory } from '../factory';
import type { IPerson } from '~~/types/person';

class PersonModule extends HttpFactory {
    private RESOURCE = '/person';

    /**
     * Fetch all persons
     */
    async getAll(): Promise<IPerson[]> {
        return await this.call<IPerson[]>('GET', `${this.RESOURCE}`);
    }

    /**
     * Delete person
     */
    async delete(id: string | number): Promise<void> {
        return await this.call<void>('DELETE', `${this.RESOURCE}/${id}`);
    }

    // async create(account: ICreateAccountInput): Promise<ICreateAccountResponse> {
    //     return await this.call<ICreateAccountResponse>('POST', `${this.RESOURCE}/register`, account);
    // }
  }

  export default PersonModule;