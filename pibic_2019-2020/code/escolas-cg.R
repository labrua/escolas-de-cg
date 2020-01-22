library(dplyr)
library(ggplot2)

escolas_iniciais <- readr::read_csv(here::here("data/ideb_anos_iniciais.csv"))

escolas_iniciais %>%
  group_by(NU_NOTA) %>%
  summarise(n = n()) %>%
  ggplot(aes(x = NU_NOTA, y = n)) +
  geom_point()
