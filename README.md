# tunnel-sandbox

Dépôt **public** d'essai du Tunnel HEXARION (voir `tunnel-core`, `docs/ARCHITECTURE.md`, révision 7).

- Il ne contient **aucun secret** et ne doit jamais en contenir : il est lisible de tous.
- C'est le seul dépôt où la fusion automatique sans relecture est activée (règles de branche gratuites sur dépôt public).
- Il sert à prouver le flux : sessions IA en parallèle, CI, file de fusion, retour arrière automatique.
- Le code (`sandbox/`) est volontairement trivial et jetable.

## CI

Le job `linux-tests` n'installe rien et ne lance rien lui-même : il appelle le harnais [tunnel-ci](https://github.com/HEXARION-Co/tunnel-ci) (`actions/run-tests`), épinglé par SHA complet, qui exécute les tests dans un conteneur sans réseau, sans secret et en lecture seule. Ce SHA est le « harnais attendu » de la porte de fusion (`ci_harness_sha`). Le modifier est un changement de juge : PR humaine uniquement.
