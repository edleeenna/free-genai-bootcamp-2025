
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { useTheme } from "@/components/theme-provider";
import { useState } from "react";

const Settings = () => {
  const { theme, setTheme } = useTheme();
  const [resetConfirmation, setResetConfirmation] = useState("");

  const handleReset = () => {
    if (resetConfirmation.toLowerCase() === "reset me") {
      console.log("Resetting database...");
      // Add reset logic here
    }
  };

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Settings</h1>
      
      <div className="space-y-8">
        <div className="flex items-center justify-between">
          <div className="space-y-1">
            <Label>Dark Mode</Label>
            <p className="text-sm text-muted-foreground">
              Enable dark mode for a better night-time experience
            </p>
          </div>
          <Switch
            checked={theme === "dark"}
            onCheckedChange={(checked) => setTheme(checked ? "dark" : "light")}
          />
        </div>

        <div className="space-y-4">
          <div className="space-y-1">
            <Label className="text-destructive">Reset History</Label>
            <p className="text-sm text-muted-foreground">
              This will permanently delete all your learning history
            </p>
          </div>
          
          <AlertDialog>
            <AlertDialogTrigger asChild>
              <Button variant="destructive">Reset Database</Button>
            </AlertDialogTrigger>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>Are you sure?</AlertDialogTitle>
                <AlertDialogDescription>
                  This action is irreversible. Type "reset me" to confirm.
                </AlertDialogDescription>
              </AlertDialogHeader>
              <Input
                value={resetConfirmation}
                onChange={(e) => setResetConfirmation(e.target.value)}
                placeholder="Type 'reset me' to confirm"
              />
              <AlertDialogFooter>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
                <AlertDialogAction
                  onClick={handleReset}
                  disabled={resetConfirmation.toLowerCase() !== "reset me"}
                >
                  Reset
                </AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        </div>
      </div>
    </div>
  );
};

export default Settings;
