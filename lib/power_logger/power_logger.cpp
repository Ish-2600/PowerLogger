// Formula SAE DC power logger
//
// The hardware measures battery/rectifier voltage and current through an
// ammeter shunt. Samples are represented in SI units to match the supplied
// test-data CSV: time_ms, voltage_v, current_a, power_w.

#include <cstdint>

namespace power_logger {

struct PowerSample {
    std::uint32_t time_ms;
    float voltage_v;
    float current_a;
};

constexpr float calculate_power_w(float voltage_v, float current_a) {
    return voltage_v * current_a;
}

}  // namespace power_logger
