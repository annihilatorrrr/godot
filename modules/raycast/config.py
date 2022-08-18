def can_build(env, platform):
    # Depends on Embree library, which only supports x86_64 and aarch64.
    if env["arch"].startswith("rv") or env["arch"].startswith("ppc"):
        return False

    if platform == "android":
        return env["android_arch"] in ["arm64v8", "x86_64"]

    return False if platform == "javascript" else env["bits"] != "32"


def configure(env):
    pass
