"""
Config file for stimulated photon emission
"""

## Common parameter definition

sequence_txt = "TwoPAC/sequences/AFC_GA_sequence.txt"
command_table = "AFC_command_table"

sequence_params = dict(

    # define HDAWG outputs
    basic_HDAWG_params = {'sampling_rate': 2.4E9,
                        'channel_AFC': 1,
                        'channel_CP' : 2,
                        'channel_SP' : 3,
                        'sequence_delay': 1E-3,
                        'burn_wait': 1E-3,
                        'AFC_wait': 1E-3,
                        'AFC_input_delay': 1E-3,
                        'read_wait' : 1E-3,
                        'shuffle_wait': 1E-3,
                        'trigger': 'read',
                        'trig_in' : 0,
                        'trig_out' : 0,
                        'trig_read' : 0},

    # Pit Pulse Parameters
    pit_params = {'no_pulses': 280,
                'f_0': 250E6,
                'amplitude': 0.12,
                'freq_sweep': 3.5E6,
                'duration': 30E-6,
                'delay': 250E-6,
                'phase': 0},

    # Burn Back Parameters
    burn_back_params = {'no_pulses': 160,
                        'f_0': 268.45E6,
                        'amplitude': 0.0395,
                        'freq_sweep': 1E6,
                        'duration': 48E-6,
                        'delay': 250E-6,
                        'phase': 0},

    # AFC Pulse Params
    AFC_params = {'no_pulses': 250, 
                'tau': 1E-6,
                'f_0': 250E6,
                'amplitude': 0.015,
                'duration': 80E-6,
                'delay': 5E-6,
                'phase': 0},

    # Reading Pulse Params
    read_params = {'f_0': 250E6,
                    'amplitude': 0.015,
                    'freq_sweep': 2.5E6,
                    'duration': 1000E-6,
                    'phase': 0},

    # Shuffle Pulse Params
    shuffle_params = {'f_0': 250E6,
                    'amplitude': 0.2,
                    'freq_sweep': 10.5E6,
                    'duration': 1000E-6,
                    'delay': 1000E-6,
                    'phase': 0}

)

# Generate AFC values
delta = 1/sequence_params['AFC_params']['tau']
no_teeth = round((4*sequence_params['burn_back_params']['freq_sweep'])/delta) + 2
no_holes = no_teeth - 1

sequence_params['AFC_params']['delta'] = delta
sequence_params['AFC_params']['no_teeth'] = no_teeth
sequence_params['AFC_params']['no_holes'] = no_holes

# Update trigger values depending on condition
if sequence_params['basic_HDAWG_params']['trigger'] == 'read':
    sequence_params['basic_HDAWG_params']['trig_read'] = 1
elif sequence_params['basic_HDAWG_params']['trigger'] == 'input':
    sequence_params['basic_HDAWG_params']['trig_in'] = 1
else:
    sequence_params['basic_HDAWG_params']['trig_out'] = 1