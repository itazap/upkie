// SPDX-License-Identifier: Apache-2.0
// Copyright 2022 Stéphane Caron

#include "upkie/cpp/utils/math.h"

#include "gtest/gtest.h"

namespace upkie::utils {

TEST(Math, Divides) {
  ASSERT_FALSE(math::divides(1000000u, 0u));
  ASSERT_FALSE(math::divides(100000u, 42u));
  ASSERT_TRUE(math::divides(100u, 20u));
}

}  // namespace upkie::utils
