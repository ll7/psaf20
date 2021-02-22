# Competition Manger

1. start carla server
   - `cd ~/carla0.9.10.1`
   - `./CarlaUE4.sh`
2. start ego vehicle
   - roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch
3. load start and goal yaml file to rosparam
   - [how to load a yaml file](config/How_to_load_yaml.md)
4. start set_position server
   - `rosrun psaf20_competition_manager set_position_server.py`
5. request setting position
   - `rosrun psaf20_competition_manager set_position_client.py`
