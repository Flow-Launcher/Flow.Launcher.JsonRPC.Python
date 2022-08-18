from RPC import RPC


class FlowLauncherAPI:
    @classmethod
    def change_query(cls, query, requery: bool = False):
        """
        change flow launcher query
        """
        RPC(
            method="Flow.Launcher.ChangeQuery",
            parameters=[query, requery],
        ).to_string()

    @classmethod
    def shell_run(cls, cmd):
        """
        run shell commands
        """
        RPC(
            method="Flow.Launcher.ShellRun",
            parameters=[cmd],
        ).to_string()

    @classmethod
    def close_app(cls):
        """
        close flow launcher
        """
        RPC(method="Flow.Launcher.CloseApp").to_string()

    @classmethod
    def hide_app(cls):
        """
        hide flow launcher
        """
        RPC(method="Flow.Launcher.HideApp").to_string()

    @classmethod
    def show_app(cls):
        """
        show flow launcher
        """
        RPC(method="Flow.Launcher.ShowApp").to_string()

    @classmethod
    def show_msg(cls, title: str, sub_title: str, ico_path: str = ""):
        """
        show messagebox
        """
        RPC(
            method="Flow.Launcher.ShowMsg",
            parameters=[
                title,
                sub_title,
                ico_path,
            ],
        ).to_string()

    @classmethod
    def open_setting_dialog(cls):
        """
        open setting dialog
        """
        RPC(method="Flow.Launcher.OpenSettingDialog").to_string()

    @classmethod
    def start_loadingbar(cls):
        """
        start loading animation in flow launcher
        """
        RPC(method="Flow.Launcher.StartLoadingBar").to_string()

    @classmethod
    def stop_loadingbar(cls):
        """
        stop loading animation in flow launcher
        """
        RPC(method="Flow.Launcher.StartLoadingBar").to_string()

    @classmethod
    def reload_plugins(cls):
        """
        reload all flow launcher plugins
        """
        RPC(method="Flow.Launcher.ReloadPlugins").to_string()
