from __future__ import annotations

import click


@click.command("init", help="Create or migrate the configuration")
@click.option(
    "--create-certs",
    "-c",
    default=None,
    help="Create new SSL certificates based on CA in [directory]",
    type=click.Path(),
)
@click.option(
    "--fix-ssl-permissions",
    is_flag=True,
    help="Attempt to fix SSL certificate/key file permissions",
)
@click.option("--testnet", is_flag=True, help="Configure this xxch install to connect to the testnet")
@click.option("--set-passphrase", "-s", is_flag=True, help="Protect your keyring with a passphrase")
@click.option(
    "--v1-db",
    is_flag=True,
    help="Initialize the blockchain database in v1 format (compatible with older versions of the full node)",
)
@click.pass_context
def init_cmd(
    ctx: click.Context,
    create_certs: str,
    fix_ssl_permissions: bool,
    testnet: bool,
    set_passphrase: bool,
    v1_db: bool,
) -> None:
    """
    Create a new configuration or migrate from previous versions to current

    \b
    Follow these steps to create new certificates for a remote harvester:
    - Make a copy of your Farming Machine CA directory: ~/.xxch/[version]/config/ssl/ca
    - Shut down all xxch daemon processes with `xxch stop all -d`
    - Run `xxch init -c [directory]` on your remote harvester,
      where [directory] is the the copy of your Farming Machine CA directory
    - Get more details on remote harvester on Xxch wiki:
      https://github.com/Chia-Network/chia-blockchain/wiki/Farming-on-many-machines
    """
    from pathlib import Path

    from xxch.cmds.passphrase_funcs import initialize_passphrase

    from .init_funcs import init

    if set_passphrase:
        initialize_passphrase()

    init(
        Path(create_certs) if create_certs is not None else None,
        ctx.obj["root_path"],
        fix_ssl_permissions,
        testnet,
        v1_db,
    )


if __name__ == "__main__":
    from xxch.util.default_root import DEFAULT_ROOT_PATH

    from .init_funcs import xxch_init

    xxch_init(DEFAULT_ROOT_PATH)
