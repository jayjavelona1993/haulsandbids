import {NavigationMenu, NavigationMenuContent, NavigationMenuLink, NavigationMenuList, NavigationMenuItem} from "@/components/ui/navigation-menu.jsx";

const NavBar = () => {

    return (
    <NavigationMenu>
        <NavigationMenuList>
            <NavigationMenuItem>
                <NavigationMenuLink>
                    Hauls
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink>
                    List Your Pickup
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink>
                    Carrier Network
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink>
                    Leaderboard
                </NavigationMenuLink>
            </NavigationMenuItem>
        </NavigationMenuList>
    </NavigationMenu>);
};

export default NavBar;