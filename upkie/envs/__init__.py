#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

import gymnasium as gym

from .upkie_base_env import UpkieBaseEnv
from .upkie_ground_velocity import UpkieGroundVelocity
from .upkie_servos import UpkieServos


def register() -> None:
    """!
    Register Upkie environments with Gymnasium.
    """
    envs = (
        ("UpkieGroundVelocity", UpkieGroundVelocity),
        ("UpkieServos", UpkieServos),
    )
    for env_name, env_class in envs:
        gym.envs.registration.register(
            id=f"{env_name}-v{env_class.version}",
            entry_point=f"upkie.envs:{env_name}",
        )


__all__ = [
    "UpkieBaseEnv",
    "register",
    "UpkieGroundVelocity",
    "UpkieServos",
]
