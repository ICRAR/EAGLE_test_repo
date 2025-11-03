# Release procedure 

The `main` branch for this repository is protected and merges to `main` require a Pull Request. 

There following steps to produce a release for a test graph updates: 

1. Merge recent feature branch into `main`. 
1. Ensure all tests pass, including tests on reciprocal DALiuGE pull request (if relevant)
3. Branch locally from `main` to branch `vx.x.x`
4. Update version in `setup.py`
5. Run `make release` and use the chosen `vx.x.x` version number.
6. Create a new Pull Request in Github, confirm details are correct, and merge. 

