export interface IEstate {
    id: number;
    name: string;
    code: string;
}

export interface IMunicipality {
    id: number;
    name: string;
    code: string;
    estate_id: Array<unknown>;
}

export interface IParish {
    id: number;
    name: string;
    code: string;
    municipality_id: Array<unknown>;
}