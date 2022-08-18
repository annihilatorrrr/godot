def can_build(env, platform):
    return env["openxr"] if platform in ["linuxbsd", "windows"] else False


def configure(env):
    pass


def get_doc_classes():
    return [
        "OpenXRInterface",
        "OpenXRAction",
        "OpenXRActionSet",
        "OpenXRActionMap",
        "OpenXRInteractionProfile",
        "OpenXRIPBinding",
    ]


def get_doc_path():
    return "doc_classes"
