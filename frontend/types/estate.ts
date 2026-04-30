export interface IEstate {
    id: number;
    name: string;
    code: string;
}

export interface IMunicipality {
    id: number;
    name: string;
    code: string;
    estate: Array<unknown>;
}