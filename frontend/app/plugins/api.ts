import { $fetch, type FetchOptions } from 'ofetch';
import { defineNuxtPlugin } from '#app';
import PersonModule from '~~/repository/modules/person';

/** ApiInstance interface provides us with good typing */
interface IApiInstance {
  person: PersonModule
}

export default defineNuxtPlugin((nuxtApp) => {


    const config = useRuntimeConfig();

    // 1. Setup fetch options (Base URL, Headers, etc.)
    const fetchOptions: FetchOptions = {
        baseURL: config.public.apiBase || 'http://127.0.0.1:8000/api',
        onResponseError({ response }) {
        console.error('API Error:', response.status, response._data);
        }
    };

    // 2. Create the fetch instance
    const apiFetcher = $fetch.create(fetchOptions);

    // 3. Initialize your modules
    const modules: IApiInstance = {
        person: new PersonModule(apiFetcher),
        // You can add more modules here as you grow (e.g., auth: new AuthModule(apiFetcher))
    };

    // 4. Inject the modules into the Nuxt App
    return {
        provide: {
        api: modules,
        },
    };
});