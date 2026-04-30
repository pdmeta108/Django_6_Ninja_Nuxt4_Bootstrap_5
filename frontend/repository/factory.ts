import type { $Fetch } from 'nitro';

export type { $Fetch };

type method = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';


export class HttpFactory {
  private $fetch: $Fetch;

  constructor(fetcher: $Fetch) {
    this.$fetch = fetcher;
  }

  /**
    * method - GET, POST, PUT
    * URL
  **/
  async call<T>(method: method, url: string, data?: object, extras = {}): Promise<T> {
    const $res: T = await this.$fetch(url, { method, body: data, ...extras });
    return $res;
  }
}