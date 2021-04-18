defmodule Slave do
  use GenServer
  @ip '52.49.91.111'
  @port 2092

  defstruct [
    :socket,
    :server_id,
    :siblings_ids,
    :parent
  ]

  def start_link(parent) do
    GenServer.start_link(__MODULE__, parent)
  end

  def init(parent) do
    result = :gen_tcp.connect(@ip, @port, [:binary, active: false])
    schedule_tick()

    {:ok, %__MODULE__{socket: result, server_id: nil, siblings_ids: [], parent: parent}}
  end

  def handle_info(:next_tick, %__MODULE__{} = state) do
    # do things
    schedule_tick()
    {:noreply, state}
  end

  defp schedule_tick() do
    Process.send_after(self(), :next_tick, 5)
  end

  defp read_line() do

  end
end
