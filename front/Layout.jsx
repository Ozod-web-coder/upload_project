import Header from "./src/components/header/Header.jsx";
import { Outlet } from 'react-router-dom';
export default function Layout() {
    return (
        <>
            <Header />
            <div className={"ml-64 p-6"}>
                <Outlet />
            </div>

        </>
    );
}