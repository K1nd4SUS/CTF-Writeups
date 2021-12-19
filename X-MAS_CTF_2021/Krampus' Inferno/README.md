# Krampus' Inferno

## Description

Two elf-bots from Santa's Laboratory have been kidnapped by his archenemy, Krampus. What is this weird demon up to this time around?

`nc challs.xmas.htsp.ro 5005`

## Solution

```
std::pair<int, int> bot666013(uint8_t board[8][8], std::pair<int, int> magic_coin) {
    int h = magic_coin.first * 8 + magic_coin.second;
    for (int x = 0; x < 8; x++) {
        for (int y = 0; y < 8; y++) {
            h ^= board[x][y] * (8 * x + y);
        }
    }
    return std::make_pair(h / 8, h % 8);
}

std::pair<int, int> bot1000000007(uint8_t board[8][8]) {
    int h = 0;
    for (int x = 0; x < 8; x++) {
        for (int y = 0; y < 8; y++) {
            h ^= board[x][y] * (8 * x + y);
        }
    }
    return std::make_pair(h / 8, h % 8);
}
```


#### **FLAG >>** `X-MAS{B07_t34mw0rk_d3f3475_Kr4mpu5}`