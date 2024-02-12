import { useState } from "react";

export interface CustomState<T> {
    get: () => T;
    set: (value: T) => void;
}

export function useCustomState<T>(initialValue: T): CustomState<T>{
    const [state, set] = useState(initialValue);
    const get = () => {
        return state;
    };

    return { get, set };
}

export interface LoginData {
    username: string | null;
    jwt: string | null;
    name: string | null;
    email: string | null;
    id: string | null;
    school: string | null;
    classes: string[] | null;
    profilePicUrl: string | null;
    isLogged: boolean;
}

export interface SignUpData {
    name: string;
    email: string;
    username: string;
    password: string;
    confirmPassword: string;
}

export class LoginState implements LoginData {
    username: string | null;
    isLogged: boolean;
    jwt: string | null;
    name: string | null;
    email: string | null;
    id: string | null;
    school: string | null;
    classes: string[] | null;
    profilePicUrl: string | null;
    constructor(
        username: string | null = null,
        jwt: string | null = null,
        name: string | null = null,
        email: string | null = null,
        id: string | null = null,
        school: string | null = null,
        classes: string[] | null = null,
        profilePicUrl: string | null = null,
        isLogged: boolean = false,
    ) {
        this.isLogged = isLogged;
        this.username = username;
        this.jwt = jwt;
        this.name = name;
        this.email = email;
        this.id = id;
        this.school = school;
        this.classes = classes;
        this.profilePicUrl = profilePicUrl;
    }
}

export type activePage = "login" | "signup" | "home" | "profile" | "class" | "settings" | "logout" | "loading";