from tkinter import *
class PhysicsCalculator:
    def __init__(self, master):
        self.master = master
        master.title("PHYSICS PLAYGROUND")

        # Create labels for the input boxes
        Label(master, text="Mass (kg)").grid(row=0)
        Label(master, text="Displacement/h(m)").grid(row=1)
        Label(master, text="Velocity (m/s)").grid(row=2)
        Label(master, text="acceleration(m/s^2)").grid(row=3)
        #Label(master, text="Final Velocity (m/s)").grid(row=2)
        Label(master, text="Time(s)").grid(row=4)
        Label(master, text="molar_mass").grid(row=5)
        Label(master, text="Force(N)").grid(column=2,row=0)
        # Label(master, text="Momentum(kg*m/s)").grid(column=2,row=1)
        # Label(master, text="Kinetic(J)").grid(column=2,row=2)
        # Label(master, text="Potential(J)").grid(column=2,row=3)

        # Create input boxes
        self.mass_entry = Entry(master)
        self.mass_entry.grid(row=0, column=1)

        self.displacement_entry = Entry(master)
        self.displacement_entry.grid(row=1, column=1)

        self.initial_velocity_entry = Entry(master)
        self.initial_velocity_entry.grid(row=2, column=1)

        #self.final_velocity_entry = Entry(master)
        #self.final_velocity_entry.grid(row=2, column=1)

        self.Acceleration_entry = Entry(master)
        self.Acceleration_entry.grid(row=3, column=1)

        self.time_entry = Entry(master)
        self.time_entry.grid(row=4, column=1)

        self.molar_mass_entry = Entry(master)
        self.molar_mass_entry.grid(row=5, column=1)

        self.Force_entry = Entry(master)
        self.Force_entry.grid(row=0, column=3)

        # self.Momentum_entry = Entry(master)
        # self.Momentum_entry.grid(row=1, column=3)

        # self.Kinetic_entry = Entry(master)
        # self.Kinetic_entry.grid(row=2, column=3)

        # self.Potential_entry = Entry(master)
        # self.Potential_entry.grid(row=3, column=3)

        #self.mass_entry = Entry(master)
        #self.mass_entry.grid(row=3, column=4)

        
        
        # Create buttons to calculate force, velocity, and acceleration
        self.calculate_force_button = Button(master, text="Calculate Force", command=self.calculate_force)
        self.calculate_force_button.grid(row=8, column=0)

        self.calculate_velocity_button = Button(master, text="Calculate Avg.Velocity", command=self.calculate_velocity)
        self.calculate_velocity_button.grid(row=8, column=1)

        self.calculate_acceleration_button = Button(master, text="Calculate Acceleration", command=self.calculate_acceleration)
        self.calculate_acceleration_button.grid(row=8, column=2)

        self.calculate_momentum_button = Button(master, text="Calculate momentum", command=self.calculate_momentum) 
        self.calculate_momentum_button.grid(row=8, column=3)

        self.calculate_kinetic_button = Button(master, text="Calculate kinetic", command=self.calculate_kinetic) 
        self.calculate_kinetic_button.grid(row=8, column=4)

        self.calculate_potential_button = Button(master, text="Calculate potential", command=self.calculate_potential) 
        self.calculate_potential_button.grid(row=8, column=5)

        self.calculate_moles_button = Button(master, text="Calculate moles", command=self.calculate_moles) 
        self.calculate_moles_button.grid(row=8, column=6)

        self.calculate_mass_button = Button(master, text="Calculate mass", command=self.calculate_mass) 
        self.calculate_mass_button.grid(row=8, column=7)

        # Create labels to display the results
        self.force_label = Label(master, text="")
        self.force_label.grid(row=6, column=0)

        self.velocity_label = Label(master, text="")
        self.velocity_label.grid(row=6, column=1)

        self.acceleration_label = Label(master, text="")
        self.acceleration_label.grid(row=6, column=2)

        self.momentum_label = Label(master, text="")
        self.momentum_label.grid(row=6, column=3)

        self.kinetic_label = Label(master, text="")
        self.kinetic_label.grid(row=6, column=4)

        self.potential_label = Label(master, text="")
        self.potential_label.grid(row=6, column=5)

        self.moles_label = Label(master, text="")
        self.moles_label.grid(row=6, column=6)

        self.mass_label = Label(master, text="")
        self.mass_label.grid(row=6, column=7)

    def calculate_force(self):
        try:
            mass = float(self.mass_entry.get())
            Acceleration = float(self.Acceleration_entry.get())
            #acceleration = (float(self.final_velocity_entry.get()) - float(self.initial_velocity_entry.get())) / float(self.time_entry.get())
            force = mass * Acceleration
            self.force_label.config(text=f"The force is {force:.2f} N")
        except ValueError:
            self.force_label.config(text="Invalid input")

    def calculate_velocity(self):
        try:
            #initial_velocity = float(self.initial_velocity_entry.get())
            displacement = float(self.displacement_entry.get())
            time = float(self.time_entry.get())
            #acceleration = (float(self.final_velocity_entry.get()) - initial_velocity) / time
            #velocity = initial_velocity + acceleration * time
            velocity = displacement / time
            self.velocity_label.config(text=f"The velocity is {velocity:.2f} m/s")
        except ValueError:
            self.velocity_label.config(text="Invalid input")

    def calculate_acceleration(self):
        try:
            initial_velocity = float(self.initial_velocity_entry.get())
            #final_velocity = float(self.final_velocity_entry.get())
            time = float(self.time_entry.get())
            acceleration = ( initial_velocity) / time
            self.acceleration_label.config(text=f"The acceleration is {acceleration:.2f} m/s^2")
        except ValueError:
            self.acceleration_label.config(text="Invalid input")

    def calculate_momentum(self):
        try:
            mass = float(self.mass_entry.get())
            initial_velocity = float(self.initial_velocity_entry.get())
            #acceleration = (float(self.final_velocity_entry.get()) - float(self.initial_velocity_entry.get())) / float(self.time_entry.get())
            momentum = mass * initial_velocity
            self.momentum_label.config(text=f"The momentum is {momentum:.2f} kg*m/s")
        except ValueError:
            self.momentum_label.config(text="Invalid input")

    def calculate_kinetic(self):
        try:
            initial_velocity = float(self.initial_velocity_entry.get())
            #final_velocity = float(self.final_velocity_entry.get())
            mass = float(self.mass_entry.get())
            kinetic = 0.5 * mass * initial_velocity * initial_velocity
            #acceleration = ( initial_velocity) / time
            #self.acceleration_label.config(text=f"The acceleration is {acceleration:.2f} m/s^2")
            self.kinetic_label.config(text=f"The kinetic is {kinetic:.2f} kg*m^2/s^2")
        except ValueError:
            self.kinetic_label.config(text="Invalid input")

    def calculate_potential(self):
        try:
            mass = float(self.mass_entry.get())
            #acceleration = ( initial_velocity) / time
            Acceleration = float(self.Acceleration_entry.get())
            displacement = float(self.displacement_entry.get())
            potential = mass * Acceleration * displacement
            self.potential_label.config(text=f"The potential is {potential:.2f} kg*m/s^2*m")
        except ValueError:
            self.potential_label.config(text="Invalid input")

    def calculate_moles(self):
        try:
            mass = float(self.mass_entry.get())
            molar_mass = float(self.molar_mass_entry.get())
            moles = mass / molar_mass
            self.moles_label.config(text=f"The moles is {moles:.2f}")
        except ValueError:
            self.moles_label.config(text="Invalid input")

    def calculate_mass(self):
        try:
            force = float(self.Force_entry.get())
            acceleration = float(self.Acceleration_entry.get())
            # Momentum = float(self.Momentum_entry.get())
            # velocity = float(self.initial_velocity_entry.get())
            # mass = Momentum / velocity
            mass = force / acceleration
            self.mass_label.config(text=f"The mass is {mass:.2f}")
            
        except ValueError:
             self.mass_label.config(text="Invalid input")       

    


# Create the Tkinter window and start the app
root = Tk()
app = PhysicsCalculator(root)
root.mainloop()


