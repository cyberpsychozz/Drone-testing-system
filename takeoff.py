from pymavlink import mavutil
import time
# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14550')

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, 
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,1,0,0,0,0,0,0)

msg = the_connection.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,15)

msg = the_connection.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)

time.sleep(5)

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, 
                                     mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0)

msg = the_connection.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)

# msg = the_connection.recv_match(type='ALTITUDE',blocking=True)
# print(msg)

# the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, 
#                                      mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,0,0,0,0,0,0,0)

# msg = the_connection.recv_match(type='COMMAND_ACK',blocking=True)
# print(msg)