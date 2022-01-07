# testing_UR5

Test for study about gazebo for UR5

-----------------------

## Important Point

When construct about moveit planning, 


**Must Delete line 21 of "trajectory_execution.launch.xml" in $(myrobot_moveit_config)/launch** 
 
 > < arg name="execution_type" value="$(arg execution_type)" />
 
