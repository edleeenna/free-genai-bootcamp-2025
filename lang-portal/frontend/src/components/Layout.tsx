
import { Outlet, useLocation, Link } from "react-router-dom";
import { cn } from "@/lib/utils";
import {
  Book,
  Layers,
  Layout as LayoutIcon,
  Settings as SettingsIcon,
  Timer,
  GraduationCap,
} from "lucide-react";

const navigation = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutIcon },
  { name: "Study Activities", href: "/study-activities", icon: GraduationCap },
  { name: "Words", href: "/words", icon: Book },
  { name: "Word Groups", href: "/groups", icon: Layers },
  { name: "Sessions", href: "/sessions", icon: Timer },
  { name: "Settings", href: "/settings", icon: SettingsIcon },
];

const Layout = () => {
  const location = useLocation();

  const getBreadcrumbs = () => {
    const paths = location.pathname.split("/").filter(Boolean);
    return paths.map((path, index) => {
      const url = `/${paths.slice(0, index + 1).join("/")}`;
      const isLast = index === paths.length - 1;
      const name = path.split("-").map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
      ).join(" ");

      return (
        <div key={url} className="flex items-center">
          {index > 0 && (
            <span className="mx-2 text-gray-400">/</span>
          )}
          {isLast ? (
            <span className="text-japanese-600 font-medium">{name}</span>
          ) : (
            <Link
              to={url}
              className="text-gray-500 hover:text-japanese-500 transition-colors"
            >
              {name}
            </Link>
          )}
        </div>
      );
    });
  };

  return (
    <div className="min-h-screen bg-background">
      <nav className="border-b bg-card shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  to={item.href}
                  className={cn(
                    "inline-flex items-center px-4 border-b-2 text-sm font-medium transition-colors",
                    location.pathname === item.href
                      ? "border-japanese-500 text-japanese-600"
                      : "border-transparent text-gray-500 hover:text-japanese-500 hover:border-japanese-300"
                  )}
                >
                  <item.icon className="h-4 w-4 mr-2" />
                  {item.name}
                </Link>
              ))}
            </div>
          </div>
        </div>
      </nav>
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex text-sm mb-6">
          {getBreadcrumbs()}
        </div>
        <main>
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default Layout;
