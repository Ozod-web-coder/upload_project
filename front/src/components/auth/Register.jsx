'use client'

import { useState } from "react"
import axios from "axios"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"

// Схема валидации
const schema = z.object({
    username: z.string().min(3, "Минимум 3 символа"),
    password: z.string().min(6, "Минимум 6 символов")
})

export default function AuthForm() {
    const [isLogin, setIsLogin] = useState(true)
    const [message, setMessage] = useState("")

    const {
        register,
        handleSubmit,
        formState: { errors }
    } = useForm({
        resolver: zodResolver(schema)
    })

    const onSubmit = async (data) => {
        try {
            const url = isLogin
                ? "http://localhost:8000/login"
                : "http://localhost:8000/register"

            const response = await axios.post(url, data)

            if (response.status === 200) {
                setMessage(isLogin ? "Успешный вход" : "Регистрация прошла успешно")
                console.log("Ответ сервера:", response.data)
                localStorage.setItem("token",response.data.access_token)
            } else {
                setMessage("Ошибка: " + response.statusText)
            }
        } catch (error) {
            console.error(error)
            setMessage("Ошибка: " + (error.response?.data?.message || "Сервер недоступен"))
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-sky-100 to-blue-200 px-4">
            <div className="w-full max-w-md bg-white rounded-3xl shadow-2xl p-8 space-y-6">
                <h2 className="text-2xl font-bold text-center text-gray-800">
                    {isLogin ? "Вход в аккаунт" : "Создание аккаунта"}
                </h2>

                <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Логин</label>
                        <input
                            type="text"
                            {...register("username")}
                            className="w-full px-4 py-2 mt-1 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-400"
                            placeholder="Введите логин"
                        />
                        {errors.login && <p className="text-sm text-red-500 mt-1">{errors.login.message}</p>}
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700">Пароль</label>
                        <input
                            type="password"
                            {...register("password")}
                            className="w-full px-4 py-2 mt-1 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-400"
                            placeholder="••••••••"
                        />
                        {errors.password && <p className="text-sm text-red-500 mt-1">{errors.password.message}</p>}
                    </div>

                    <button
                        type="submit"
                        className="w-full bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700 transition font-semibold"
                    >
                        {isLogin ? "Войти" : "Зарегистрироваться"}
                    </button>
                </form>

                {message && (
                    <p className="text-sm text-center text-red-600 font-medium">{message}</p>
                )}

                <p className="text-sm text-center text-gray-600">
                    {isLogin ? "Нет аккаунта?" : "Уже зарегистрированы?"}{" "}
                    <button
                        onClick={() => {
                            setIsLogin(!isLogin)
                            setMessage("")
                        }}
                        className="text-blue-600 hover:underline font-medium"
                    >
                        {isLogin ? "Регистрация" : "Войти"}
                    </button>
                </p>
            </div>
        </div>
    )
}
