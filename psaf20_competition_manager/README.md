# Competition Manger

1. start carla server
   - `cd ~/carla0.9.10.1`
   - `./CarlaUE4.sh`
2. load town

```python
import carla
client = carla.Client('localhost', 2000)
client.set_timeout(10.0) # seconds
world = client.load_world('Town05')
```

3. start ego vehicle
   - `roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch vehicle_filter:=model3`
4. load start and goal yaml file to rosparam
   - [how to load a yaml file](config/How_to_load_yaml.md)
   - `rosparam load config/Town05/town05_sg2.yaml`
5. start set_position server
   - `rosrun psaf20_competition_manager set_position_server.py`
6. request setting position
   - `rosrun psaf20_competition_manager set_position_client.py`
7. `rosrun psaf20_competition_manager simple_competition_manager.py`
8. spawn npcs

```shell
cd carla0.9.10.1/PythonAPI/examples/
python spawn_npc.py -n 200 -w 0
```

9. `rosparam set /competition/traffic_rules false`
10. `rosparam set /competition/ready_for_ego true`

## manual position set

```shell
rostopic pub /carla/ego_vehicle/initialpose geometry_msgs/PoseWithCovarianceStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
pose:
  pose:
    position: {x: 154.44, y: -30.51, z: 0.0}
    orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}
  covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0]" -1
```
