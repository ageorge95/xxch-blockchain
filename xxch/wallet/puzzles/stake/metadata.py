from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from xxch.types.blockchain_format.sized_bytes import bytes32
from xxch.types.stake_value import get_stake_value_old
from xxch.util.ints import uint16, uint64
from xxch.util.streamable import Streamable, streamable


@streamable
@dataclass(frozen=True)
class StakeMetadata(Streamable):
    stake_type: uint16
    is_stake_farm: bool
    stake_puzzle_hash: bytes32
    recipient_puzzle_hash: bytes32

    @property
    def time_lock(self) -> uint64:
        return get_stake_value_old(self.stake_type, self.is_stake_farm).time_lock


class StakeVersion(IntEnum):
    V1 = uint16(1)


@streamable
@dataclass(frozen=True)
class AutoWithdrawStakeSettings(Streamable):
    enabled: bool = False
    tx_fee: uint64 = uint64(0)
    batch_size: uint16 = uint16(50)
