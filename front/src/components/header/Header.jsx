import React, { useState } from 'react';

export default function Header() {
    const [hovered, setHovered] = useState(false);
    const userName = 'Озод';

    return (
        <aside className="fixed top-0 left-0 h-full w-64 bg-slate-800 shadow-lg flex flex-col p-6 z-50">
        {/* Левая часть — текст */}
            <div className="flex flex-col gap-6 text-gray-100 font-medium text-lg">
                <span className="cursor-pointer hover:text-blue-400 transition-colors">Общие</span>
                <span className="cursor-pointer hover:text-blue-400 transition-colors">Мои</span>
            </div>

            {/* Нижняя часть — имя / выйти */}
            <div
                className="text-gray-100 font-semibold text-lg cursor-pointer transition mt-auto"
                onMouseEnter={() => setHovered(true)}
                onMouseLeave={() => setHovered(false)}
            >
                {hovered ? (
                    <span className="text-red-400">Выйти</span>
                ) : (
                    <span>{userName}</span>
                )}
            </div>
        </aside>
    );
}
