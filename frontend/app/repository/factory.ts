import type { $Fetch } from 'nitropack';
import type { AsyncDataOptions } from 'nuxt/app';
import type { FetchOptions } from 'ofetch';
import { joinURL } from 'ufo';
import type { z } from 'zod';

export type { $Fetch };

type Method = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';

type CallOptions<T> = {
  asyncOptions?: AsyncDataOptions<T>;
  fetchOptions?: Omit<FetchOptions, 'method' | 'body' | 'onRequest'>;
  schema?: z.ZodType<T>;
  useComposable?: boolean;
};

type GetOptions<T> = Omit<CallOptions<T>, 'fetchOptions'>;

export class HttpFactory {
  private readonly fetch: $Fetch;
  protected resource: string;

  constructor(fetch: $Fetch, resource = '') {
    this.fetch = fetch;
    this.resource = resource;
  }

  protected async call<
    R = unknown,
    DTO extends BodyInit | Record<string, unknown> | null | undefined = Record<string, unknown>,
  >(
    method: Method,
    url: string,
    body?: DTO,
    { fetchOptions = {}, asyncOptions = {}, useComposable = true, schema }: CallOptions<R> = {},
  ) {
    const fullPath = joinURL(this.resource, url);
    const options = {
      method,
      body,
      ...fetchOptions,
    };

    if (useComposable) {
      return useAsyncData(async () => {
        const data = await this.fetch<R>(fullPath, options);

        return schema ? schema.parse(data) : data;
      }, asyncOptions);
    }

    const data = await this.fetch<R>(fullPath, options);

    return schema ? schema.parse(data) : data;
  }

  /**
   * A helper method for making GET requests.
   */
  protected async get<R = unknown>(
    method: Method,
    url: string,
    fetchOptions: Pick<CallOptions<R>, 'fetchOptions'>,
    { asyncOptions = {}, useComposable = true, schema }: GetOptions<R> = {},
  ) {
    const fullPath = joinURL(this.resource, url);
    const options = {
      method,
      ...fetchOptions,
    };

    if (useComposable) {
      return useAsyncData(async () => {
        const data = await this.fetch<R>(fullPath, options);

        return schema ? schema.parse(data) : data;
      }, asyncOptions);
    }

    const data = await this.fetch<R>(fullPath, options);

    return schema ? schema.parse(data) : data;
  }
}